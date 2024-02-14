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
let divise n p = p mod n = 0

let f = divise 7 28
let h = divise 6 28

(*d*)
let max3 a b c = let m1 = if a < b then a else b in if m1 < c then c else m1

let x = max3 42 54 2024
 
(*e*)
let racine a b c = 
  let d = b**2. -. 4. *. a *. c in 
  if d < 0. then 
    failwith "pas de racine réelle" 
else 
  ((-.b -. d ** 0.5) /. (2. *. a), (-.b +. d ** 0.5) /. (2. *. a)) 

let f = racine 1. 0. (-.1.)

(*Exercice 2.4*)

(*a*)
let rec somme n = match n with
| 1 -> 1
|_ -> 1/n + somme (pred n)

(*b*)
let carre n = 
  let n_2 = ref n in
  for _ = 3 to n do
    n_2 := !n_2 + n;
  done;
  n + !n_2

let carre2 n = 
  let n_2 = ref n in
  let i = ref 1 in
  while !i < pred n do
    n_2 := !n_2 + n;
    incr i;
  done;
  n + !n_2

let j = carre2 8

(*d*)
let f a n = 
  let a_n = ref a in
  for _ = 2 to n do 
    a_n := !a_n * a;
  done;
  !a_n * !a_n

let k = f 2 5
let o = f 2 6

(*Exercice 2.5*)

(*a*)
(*boucle infiny*)

(*b*)
(*1*)

(*Exercice 2.6*)

(*a*)
