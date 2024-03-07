(*Exercice 3.1*)

(*a*)
let rec fact  = function
  |0 -> 1
  |x -> x * fact (pred x)


let fact_t =
  let rec ft acc  = function
    | 0. -> acc
    | x -> ft (x *. acc) (x -. 1.)
  in ft 1. 

(*b*)
(*\sum_{0}^{\infty} \frac{1}{n!} = e *)
let rec e = function
  | 0. -> 1.
  | n -> 1. /. fact_t n +. e (n -. 1.)

let aprox_e = e 2000.

(*c*)
(*racine de 2 pi *)

(*Exercice 3.2*)

(*a*)
let rec u = function
  |0 -> 1.
  |n -> sin (u (pred n))

let u_30 = u 30

let aprox_u x =
  let rec a_u n v x = match v < x with
  | true -> n
  | false -> a_u (succ n) (sin v ) x
  in
  a_u 0 1.

let n_a = aprox_u 1e-3 (*2999989*)

(*Exercice 3.3*)

(*a*) 

let rec pgcd a b = match a mod b with
  | 0 -> b
  | r -> pgcd b r

(*b*)

let pgcdi a_ b_ = 
  let a = ref a_ in
  let b = ref b_ in
  while !b <> 0 do 
    let r = !a mod !b in
    a := !b;
    b := r;
  done ;
  !a

(*c*)
(*un O de ln(a) ou ln(b)*)

(*Exercice 3.4*)

(*a*) 
let rec bin = function
 |0 -> ""
 |n ->  bin (n / 2)  ^ string_of_int (n mod 2)

let t = bin 54

(*b*)
let rec int_of_bin = function
  |"0" -> 0
  |"1" -> 1
  |ch -> let len = String.length ch in 
        (int_of_bin (String.sub ch 0 (len - 1))) * 2 + int_of_char ch.[len-1]- int_of_char '0'

let u = ((((1*2 + 1)*2 + 0)*2 + 1 )*2 + 1) *2 +0
let v = int_of_bin "110110"

let int_of_bin_ter =
  let rec iobt acc = function
    |"0" -> acc*2
    |"1" -> acc * 2 + 1
    |ch -> let len = String.length ch in 
            iobt (acc * 2 + int_of_char ch.[0]- int_of_char '0') (String.sub ch 1 (len - 1))
  in
  iobt 0
let vijf= int_of_bin_ter "110110"

let int_of_bin_it ch = 