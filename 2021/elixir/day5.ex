{:ok, lines} = File.read("inputs/day5.in")

lines =
  lines
  |> String.split("\r\n", trim: true)
  |> Enum.map(fn line ->
    line
    |> String.split(" -> ", trim: true)
    |> Enum.map(&String.split(&1, ",", trim: true))
    |> Enum.reduce(&(&2 ++ &1))
    |> Enum.map(&String.to_integer/1)
  end)

h_and_v_lines =
  Enum.filter(lines, fn [x1, y1, x2, y2] ->
    x1 == x2 || y1 == y2
  end)

IO.inspect(h_and_v_lines)

line_map =
  Enum.reduce(h_and_v_lines, %{}, fn [x1, y1, x2, y2], acc ->
    if y1 == y2 do
      if x1 > x2 do
        [x1, y1, x2, y2] = [x2, y2, x1, y1]
      end

      for x <- x1..x2,
          do:
            Map.get_and_update(acc, {x, y1}, fn current ->
              {current, 1}
            end)
    else
      if y1 > y2 do
        [x1, y1, x2, y2] = [x2, y2, x1, y1]
      end

      for y <- y1..y2,
          do:
            Map.get_and_update(acc, {x1, y}, fn current ->
              {current, 1}
            end)
    end
  end)

IO.inspect(Map.get(line_map, {0, 9}))
