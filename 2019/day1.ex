# Part 1

{:ok, fuels} = File.read("day1.in")
fuels = String.split(fuels, "\r\n", trim: true)
fuels = Enum.map(fuels, fn x -> String.to_integer(x) end)
total = Enum.reduce(fuels, 0, fn x, acc -> trunc(x / 3) - 2 + acc end)
IO.puts(total)

# Part 2

{:ok, fuels} = File.read("day1.in")
fuels = String.split(fuels, "\r\n", trim: true)
fuels = Enum.map(fuels, fn x -> String.to_integer(x) end)

defmodule ReduceFuel do
  def reduce_fuel(x, acc) do
    if trunc(x / 3) - 2 <= 0 do
      acc
    else
      reduce_fuel(trunc(x / 3) - 2, trunc(x / 3) - 2 + acc)
    end
  end
end

total = Enum.reduce(fuels, 0, fn x, acc -> ReduceFuel.reduce_fuel(x, 0) + acc end)
IO.puts(total)
