{:ok, depths} = File.read("inputs/day1.in")

depths = Enum.map(String.split(depths, "\r\n", trim: true), fn d -> String.to_integer(d) end)

defmodule ReduceDepths do
  def reduce_depths([h | t], acc) do
    if length(t) <= 0 do
      acc
    else
      if h < hd(t) do
        reduce_depths(t, acc + 1)
      else
        reduce_depths(t, acc)
      end
    end
  end
end

increases = ReduceDepths.reduce_depths(depths, 0)

IO.puts(increases)

# Part 2

defmodule ReduceDepths3 do
  def reduce_depths([h | t], acc) do
    if length(t) <= 2 do
      acc
    else
      if h < hd(tl(tl(t))) do
        reduce_depths(t, acc + 1)
      else
        reduce_depths(t, acc)
      end
    end
  end
end

IO.puts(ReduceDepths3.reduce_depths(depths, 0))
