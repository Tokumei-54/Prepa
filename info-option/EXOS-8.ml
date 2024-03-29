(*Exercice 8.1*)
(*a*)
let rec takewhile f = function
  |[] -> []
  |h::t -> if f h then h :: takewhile f t else []

let test = takewhile (function n -> n mod 2 = 0) [0;2;3;4;5;6;7;8;9] 

(*b*)
let rec dropwhile f = function
  |[] -> []
  |h::t -> if f h then dropwhile f t else h::t

let test = dropwhile (function n -> n mod 2 = 0) [0;2;3;4;5;6;7;8;9] 

(*Exercice 8.2*)
(*a*)
let rec insere a = function
  |[] -> [a]
  |h::t -> if h > a then a::h::t else h::insere a t

let test = insere 4 [0;1;2;3;5;6;7;8;9] 

(*b*)
let rec tri = function
  |[] -> []
  |h::t -> insere h (tri t)

let test = tri [9;5;4;8;6;2;7;3;1;0] 


(*c*)

let trit = 
  let rec aux acc = function
    |[] -> acc
    |h::t -> aux (insere h acc) t
  in
  aux []

let test = trit [9;5;4;8;6;2;7;3;1;0] 

(*d*)
(*O(n^2)*)

(*Exercice 8.3*)

