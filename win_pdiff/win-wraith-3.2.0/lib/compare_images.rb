require "wraith"
require "stringio"
require "wraith/helpers/logger"
require "image_size"
require "open3"
require "parallel"
require "shellwords"

class Wraith::CompareImages
  include Logging
  attr_reader :wraith

  def initialize(config)
    @wraith = Wraith::Wraith.new(config)
  end

  def compare_images
    files = Dir.glob("#{wraith.directory}/*/*.png").sort
    files.each_slice(2) do |base, compare|
      diff = base.gsub(/([a-zA-Z0-9]+).png$/, "diff.png")
      info = base.gsub(/([a-zA-Z0-9]+).png$/, "data.txt")
      logger.info "Comparing #{base} and #{compare}"
      compare_task(base, compare, diff, info)
      logger.info "Saved diff as #{diff} and info as #{info}"
    end
  end

  def percentage(img_size, px_value, info)
    pixel_count = ((px_value.to_f / img_size.to_f).to_f * 100).to_f
    rounded = pixel_count.round(2)
    File.open(info, "w") { |file| file.write(rounded.to_s) }
  end

  def capture_stdout
    begin
      old_stdout = $stdout
      $stdout = StringIO.new('','w')
      $stdout.sync = true
      yield
      output = $stdout.string
    ensure
      $stdout = old_stdout
    end
    return output
  end

  def compare_task(base, compare, output, info)
    cmdline = "compare -dissimilarity-threshold 1 -fuzz #{wraith.fuzz} -metric AE -highlight-color #{wraith.highlight_color} #{base} #{compare.shellescape} #{output} 2> #{info}"
    system(cmdline)
    px_value = IO.read(info).to_f 
    begin
      img_size = ImageSize.path(output).size.inject(:*)
      percentage(img_size, px_value, info)
    rescue
      File.open(info, "w") { |file| file.write("invalid") } unless File.exist?(output)
    end
  end
end
