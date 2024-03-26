(*Exercice 5.1*)

(*a*)

let rec fn f n x = match n with
  | 0 -> x
  |_ -> f (fn f (pred n) x)

let test = fn (function x -> x + 1) 10 0 

(*b*)
let rec f2n f n = match n with
  | 0 -> (function  a -> a)
  | _ -> (function x -> fn f (pred n) (f x)) 

let test = f2n (function  x -> x + 1) 10 0 

(*Exercice 5.2*)

(*a*)
(*-> est prioritaire type cree_cpt : int -> unit -> int *)
(*b*)
(*033*)
(*test*)
(* let cree_cpt n = 
  let c = ref (n-1) in 
  function () -> incr c ; !c

let () = 
  let compteur = cree_cpt 0 in
  print_int(compteur ());
  print_int(compteur () + compteur ());
  print_int(compteur ()); *)

(*Exercice 5.3*)
(*a*)
let curryfie f a b =  f (a,b)

(*b*)
let decurryfie f (a,b) = f a b

(*Exercice 5.4*)
(*a*)

(*b*)
let m a b =
  let rec u = function 
    |0 -> a
    |n -> Printf.printf "u %d \n" n ;sqrt (u (pred n) *. v (pred n))
    and v = function
    |0 -> b 
    |n -> Printf.printf "v %d \n" n ;(u (pred n) +. v (pred n))/.2.
  in
  u 20

let test = m 100. 1000.