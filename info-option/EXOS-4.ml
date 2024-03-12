(*Exercice 4.1*)

(*a*)
let implication a b = b || not a  
let implication2 a b = if a then true else b
let g = implication false true

(*b*)
let xor a b = a||b || not a && b
(*c*)
let egalitéQ (a, b) (c,d) = a*d = b*c
(*d*)
let egalitéQ2 ((a, b),(c,d)) = a*d = b*c

(*Exercice 4.2*)
let rec f a x = match x >= float_of_int a with
  | false -> 0
  | true -> f a (x /. (float_of_int a)) + 1

let ilog2 = f 2

let v = 2048.
let t = ilog2 v
let u = (log v) /. log 2.

(*Exercice 4.3*)
(*a*)
let rec puiss x = function
  |0 -> 1
  |n -> (puiss x (pred n)) * x 
