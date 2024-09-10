let rec map f = function 
 | [] -> []
 | h::t -> f h :: (map f t)

let test = map (fun x -> 2 * x) [0;1;2;3;4;5;6;7;8;9]

let rec iter f = function
  |[] -> ()
  |h::t -> f h ; iter f t

let test2 = iter (fun x -> print_int x) [0;1;2;3;4;5;6;7;8;9]

let rec filter f = function
  |[] -> []
  |h::t -> if f h then h:: filter f t else filter f t

let test3 = filter (fun x -> x mod 2 = 0) [0;1;2;3;4;5;6;7;8;9]

let rec for_all f = function
  |[] -> true 
  |h::t -> f h && for_all f t

let test4 = for_all (fun x -> x mod 2 = 0) [0;1;2;3;4;5;6;7;8;9]

let rec fold_left f acc = function
  |[] -> acc
  |h::t -> fold_left f (f acc h) t

let test5 = fold_left (+) 0  [0;1;2;3;4;5;6;7;8;9]

let rec fold_right f acc = function
  |[] -> acc
  |h::t -> f (fold_right f acc t) h

let test6 = fold_right (+) 0  [0;1;2;3;4;5;6;7;8;9]

let sum = fold_left (+) 0

let moyenne l = float_of_int (sum l) /. float_of_int (List.length l)

let test7 = moyenne [0;1;2;3;4;5;6;7;8;9]

let rec est_trie = function
  |[] | _::[] -> true
  |a::b::t -> a <= b && est_trie (b::t)

let test8 = est_trie [0;1;2;3;4;5;6;7;8;9]

let rec dans x l = match l with
    |[] -> false
    |h::t -> h = x || dans x t

let doublon =
  let rec aux acc = function
    |[] -> false
    |h::t ->  dans h acc || aux (h::acc) t
  in
  aux []

  let test8 = doublon [0;1;2;3;4;5;6;7;8;9]

