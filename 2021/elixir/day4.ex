{:ok, lines} = File.read("inputs/day4.in")

lines = lines |> String.split("\r\n\r\n", trim: true)

[numbers | boards] = lines

numbers =
  numbers
  |> String.split(",", trim: true)
  |> Enum.map(&String.to_integer/1)

boards =
  boards
  |> Enum.map(fn board_str ->
    board_str
    |> String.split("\r\n", trim: true)
    |> Enum.map(fn line ->
      line
      |> String.split(" ", trim: true)
      |> Enum.map(&String.to_integer/1)
      |> Enum.map(&{&1, 0})
    end)
    |> Enum.reduce(&(&2 ++ &1))
  end)

defmodule Day4 do
  def check_win(board) do
    horizontals = Enum.chunk_every(board, 5)
    verticals = for n <- 0..4, do: Enum.take_every(Enum.slice(board, n, 25 - n), 5)

    (horizontals ++ verticals)
    |> Enum.map(fn line ->
      Enum.reduce(line, 0, fn {_, count}, acc -> acc + count end) == 5
    end)
    |> Enum.any?()
  end

  def first_win(boards, [curr_number | t]) do
    boards =
      Enum.map(boards, fn board ->
        Enum.map(board, fn {n, count} ->
          if n == curr_number do
            {n, 1}
          else
            {n, count}
          end
        end)
      end)

    winner = Enum.filter(boards, &check_win/1)

    case Enum.count(winner) do
      1 ->
        {Enum.at(winner, 0), curr_number}

      _ ->
        first_win(boards, t)
    end
  end

  def last_win(boards, [curr_number | t]) do
    boards =
      Enum.map(boards, fn board ->
        Enum.map(board, fn {n, count} ->
          if n == curr_number do
            {n, 1}
          else
            {n, count}
          end
        end)
      end)

    non_winners = Enum.filter(boards, &(not check_win(&1)))

    case Enum.count(non_winners) do
      0 ->
        {Enum.find(boards, &check_win/1), curr_number}

      _ ->
        last_win(non_winners, t)
    end
  end

  def score_board(board, curr_number) do
    zero_sum =
      board
      |> Enum.map(fn {n, count} -> if count == 0, do: n, else: 0 end)
      |> Enum.sum()

    zero_sum * curr_number
  end

  def part1(boards, numbers) do
    {board, curr_number} = Day4.first_win(boards, numbers)
    Day4.score_board(board, curr_number)
  end

  def part2(boards, numbers) do
    {board, curr_number} = Day4.last_win(boards, numbers)
    Day4.score_board(board, curr_number)
  end
end

IO.inspect(Day4.part1(boards, numbers))
IO.inspect(Day4.part2(boards, numbers))
