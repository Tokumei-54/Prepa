(*Exercice 2.1*)

(*a*)
let rec prod a b = 
  if a < b then
    b * prod a (pred b)
  else 
    a

let x = prod 3 5    

(*b*)
let dec x = String.length (string_of_int x)

let rec dec2 x = match x /10 with
| 0 -> 1
| _ -> 1 + dec2 (x/10)

(* let rec dec3 x =  match x asr 1 with
| 0 -> 1
| _ -> 1 + dec3 (x asr 1) *)

let y = dec2 2024

(*Exercice 2.3*)

(*a*)
let abso x = 
  if x < 0. then
    -. x
  else 
    x

let w = abso (-. 3.5)

(*b*)
let norme x y = (x**2. +. y**2.)**0.5
let k = norme 3. 4.

(*c*)
let divise n p = n mod p = 0

let f = divise 7 28