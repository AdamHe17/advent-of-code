{:ok, line} = File.read("inputs/day7.in")

line =
  line
  |> String.split(",", trim: true)
  |> Enum.map(&String.to_integer/1)
  |> Enum.sort()

{min, max} = Enum.min_max(line)

p1_diff =
  Enum.map(min..max, fn n ->
    Enum.reduce(line, 0, fn i, acc ->
      acc + abs(i - n)
    end)
  end)
  |> Enum.min()

p2_diff =
  Enum.map(min..max, fn n ->
    Enum.reduce(line, 0, fn i, acc ->
      x = abs(i - n)
      acc + div(x * (x + 1), 2)
    end)
  end)
  |> Enum.min()

IO.inspect([p1_diff, p2_diff])
