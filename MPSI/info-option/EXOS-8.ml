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
(*a*)
let rec valuation p n = if n mod p = 0 then 1 + valuation p (n/p) else 0

let test = valuation 2 8

(*b*)
let factorise n = 
  let v n p = valuation p n in
  let rec fac = function
    |[] -> []
    |h::t -> v n h :: fac t
  in
  fac

let test = factorise 12 [2;3;5;7;11;]

let rec prime m = function
  |[] -> true
  |h::t -> m mod h <> 0 && prime m t

let rec primes n acc m= 
   if float_of_int m > sqrt (float_of_int n) then acc 
      else if prime m acc then primes n (m::acc) (succ m)
            else primes n acc (succ m) 

let decomposition n = factorise n (primes n [] 2)

let test = decomposition 24


(*Exercice 8.4*)
