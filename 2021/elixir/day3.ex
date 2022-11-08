{:ok, lines} = File.read("inputs/day3.in")

lines = lines |> String.split("\r\n", trim: true)

# Part 1

defmodule TwoLists do
  def mergeLists([h1 | t1], [h2 | t2], acc) do
    mergeLists(t1, t2, [
      [Enum.at(h1, 0) + b_to_i(h2 == 0), Enum.at(h1, 1) + b_to_i(h2 == 1)] | acc
    ])
  end

  def mergeLists([], [], acc) do
    Enum.reverse(acc)
  end

  def b_to_i(bool) do
    if bool, do: 1, else: 0
  end
end

results =
  Enum.reduce(lines, List.duplicate([0, 0], 12), fn line, acc ->
    values =
      line
      |> String.split("", trim: true)
      |> Enum.map(&String.to_integer/1)

    TwoLists.mergeLists(acc, values, [])
  end)
  |> Enum.map(fn i ->
    if Enum.at(i, 0) > Enum.at(i, 1), do: 0, else: 1
  end)

results =
  results
  |> Enum.zip(Enum.map(results, &(1 - &1)))
  |> Enum.map(&Tuple.to_list/1)
  |> Enum.zip()
  |> Enum.map(&Tuple.to_list/1)
  |> Enum.map(fn t ->
    t
    |> Enum.map(&Integer.to_string/1)
    |> Enum.join("")
    |> String.to_integer(2)
  end)
  |> Enum.reduce(&(&1 * &2))

IO.inspect(results, charlist: false)

# Part 2

defmodule Day3 do
  def reduce_list(list, ind, comp) do
    if length(list) <= 1 do
      hd(list)
    else
      counts = count_01_at_ind(list, ind, 0, 0)

      list = filter_list(list, ind, counts, comp)

      reduce_list(list, ind + 1, comp)
    end
  end

  def count_01_at_ind([h | t], ind, acc0, acc1) do
    case String.at(h, ind) do
      "0" -> count_01_at_ind(t, ind, acc0 + 1, acc1)
      "1" -> count_01_at_ind(t, ind, acc0, acc1 + 1)
    end
  end

  def count_01_at_ind([], _, acc0, acc1) do
    [acc0, acc1]
  end

  def filter_list(list, ind, [zeros | [ones]], comp) do
    condition = if comp == "less", do: ones < zeros, else: ones >= zeros

    Enum.filter(list, &(String.at(&1, ind) == if(condition, do: "1", else: "0")))
  end
end

["more", "less"]
|> Enum.map(&Day3.reduce_list(lines, 0, &1))
|> Enum.map(&String.to_integer(&1, 2))
|> Enum.reduce(&(&1 * &2))
|> IO.inspect()
