function readinput(fn)
    p1_str, p2_str = split(read(fn, String), "\n\n")
    p1_cards = parse.(Int, filter(!isempty, split(p1_str, "\n"))[2:end])
    p2_cards = parse.(Int, filter(!isempty, split(p2_str, "\n"))[2:end])
    return (reverse(p1_cards), reverse(p2_cards))
  end
  
  function score(deck)
    score = 0
    for (i, card) in enumerate(deck)
      score += i * card
    end
    return score
  end
  
  function play1(p1_cards, p2_cards)
    deck1 = copy(p1_cards)
    deck2 = copy(p2_cards)
    while !isempty(deck1) && !isempty(deck2)
      c1 = pop!(deck1)
      c2 = pop!(deck2)
      if c1 > c2
        deck1 = vcat(c2, c1, deck1)
      else
        deck2 = vcat(c1, c2, deck2)
      end
    end
    if !isempty(deck1)
      return deck1
    else
      return deck2
    end
  end
  
  function part1(p1_cards, p2_cards)
    winner_deck = play1(p1_cards, p2_cards)
    return score(winner_deck)
  end
  
  function play2(p1_cards, p2_cards) :: Tuple{Int,Int} # player and final score
    deck1 = copy(p1_cards)
    deck2 = copy(p2_cards)
    previous_states = Set{Tuple{Vector{Int},Vector{Int}}}()
    while !isempty(deck1) && !isempty(deck2)
      if (deck1, deck2) in previous_states
        return (1, score(deck2))
      end
      push!(previous_states, (copy(deck1), copy(deck2)))
      c1 = pop!(deck1)
      c2 = pop!(deck2)
      if length(deck1) >= c1 && length(deck2) >= c2
        (winner, _) = play2(deck1[end-c1+1:end], deck2[end-c2+1:end])
        # println("@test GetIncrSum(", [reverse(deck1),reverse(deck2)], ") == ", score(deck1)+score(deck2))
        # println(score(deck1)+score(deck2), " ", [deck1,deck2], " ")
   
        if winner == 1
          deck1 = vcat(c2, c1, deck1)
        else
          deck2 = vcat(c1, c2, deck2)
        end
      else
        if c1 > c2
          deck1 = vcat(c2, c1, deck1)
        else
          deck2 = vcat(c1, c2, deck2)
        end
      end
    end
    if !isempty(deck1)
      return (1, score(deck1))
    else
      return (2, score(deck2))
    end
  end
  
  function part2(p1_cards, p2_cards)
    return play2(p1_cards, p2_cards)[2]
  end
  
  function main()
    (p1_cards, p2_cards) = readinput("input.txt")
    println(part1(p1_cards, p2_cards))
    println(part2(p1_cards, p2_cards))
  end

  main()