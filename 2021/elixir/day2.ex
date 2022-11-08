{:ok, lines} = File.read("inputs/day2.in")

result =
  lines
  |> String.split("\r\n", trim: true)
  |> Enum.map(&String.split(&1, " ", trim: true))
  |> Enum.reduce(%{a: 0, h: 0, d: 0}, fn [dir | n], acc ->
    n = n |> hd |> String.to_integer()

    case dir do
      "forward" ->
        acc
        |> Map.put(:h, acc[:h] + n)
        |> Map.put(:d, acc[:d] + n * acc[:a])

      "down" ->
        acc
        |> Map.put(:a, acc[:a] + n)

      "up" ->
        acc
        |> Map.put(:a, acc[:a] - n)
    end
  end)

IO.puts(result[:h] * result[:d])
