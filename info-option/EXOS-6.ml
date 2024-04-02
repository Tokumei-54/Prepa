(*Exercice 6.1*)

(*a*)
let est_couple li = function 
  |[_;_] -> true
  | _ -> false

(*b*)
let rec dernier = function
  |[] -> failwith "liste vide"
  |[x] -> x
  |h::t -> dernier t

let test = dernier []
let test = dernier [1]
let test = dernier [1;2]

(*c*)
let rec dernier2 = function
  |[] -> failwith "liste vide"
  |[_] -> failwith "singloton"
  |[x;y] -> x,y
  |h::t -> dernier2 t

let test = dernier []
let test = dernier [1]
let test = dernier [1;2]
let test = dernier [1;2;3]

(*d*)
let rec pos = function
  |[] -> []
  |h::t -> if h < 0 then pos t else h::pos t

let test = pos []
let test = pos [-1;2;-3;4]

(*e*)
let indice_difference_max =
  let rec i_diff id idd diff = function 
    |[] -> failwith "liste vide"
    |[_] -> idd
    |a::b::c -> let d = abs (a - b) in if d > diff then i_diff  (succ id) id d (b::c) else i_diff (succ id) idd diff (b::c)
  in
  i_diff 0 0 0

let test = indice_difference_max [1;2;4;5]

(*f*)
let maximum2 = 
  let rec max2 m1 m2 = function
    |[] -> failwith "ce cas n'existe pas"
    |[x] -> if x > m1 then x , m1 else if x > m2 then m1 , x else m1 , m2
    |h::t -> if h > m1 then max2 h m1 t else if h > m2 then max2 m1 h t else max2 m1 m2 t
  in
  function 
  |[] -> failwith "liste vide"
  |[_] -> failwith "singloton"
  | a::b::c ->if a > b then max2 a b c else max2 b a c

let test = maximum2 [1;3;2;4]

(*g*)
let rec c_d_s = function  
  |[] -> failwith "liste vide"
  |[_] -> 0
  |a::b::c -> if (a > 0)  = (b > 0) then c_d_s (b::c) else c_d_s (b::c) + 1

  let test = c_d_s [1;-1;1;-1]

(*Exercice 6.2*)

(*a*)
let rec substitue x y = function
  |[] -> failwith "liste vide" 
  |[a] -> if a = x then [y] else [a]
  |h::t -> if h = x then y::substitue x y t else h::substitue x y t

let test = substitue 0 54  [0;1;0;2;0;3]

(*b*)
let rec supprime x  = function
  |[] -> failwith "liste vide" 
  |[a] -> if a = x then [] else [a]
  |h::t -> if h = x then supprime x  t else h::supprime x t

let test = supprime 0  [0;1;0;2;0;3]

(*c*)
let rec nieme n = function
  |[] -> failwith "liste vide" 
  |[x] -> if n = 0 then x else failwith "index out of range" 
  |h::t -> if n = 0 then h else nieme (pred n) t

let test = nieme 54 [0;1;2;3;4]
let test = nieme 2 [0;1;2;3;4]

(*d*)
let rec duplique n = function
  |[] -> failwith "liste vide" 
  |li -> if n = 0 then [] else li@duplique (pred n) li

let test = duplique 5 ["-","I","-"]

(*e*)
let rec quel_que_soit f = function
  |[] -> failwith "liste vide" 
  |[a] -> f a 
  |h::t -> f h && quel_que_soit f t

let f x = x >= 0

let test = quel_que_soit f [1;1;1]
let test = quel_que_soit f [1;-1;1]

(*f*)
let rec il_exist f = function
  |[] -> failwith "liste vide" 
  |[a] -> f a 
  |h::t -> f h || il_exist f t

let f x = x >= 0

let test = il_exist f [-1;-1;-1]
let test = il_exist f [-1;1;-1]

(*Exercice 6.3*)

(*a*)
let separe li = 
  let rec pair n = function
  |[] -> failwith "liste vide" 
  |[x] -> if n mod 2 = 0 then [x] else []
  |h::t -> if n mod 2 = 0 then h:: pair (pred n) t else pair (pred n) t
  in
  let rec impair n = function
  |[] -> failwith "liste vide" 
  |[x] -> if n mod 2 = 1 then [x] else []
  |h::t -> if n mod 2 = 1 then h:: impair (pred n) t else impair (pred n) t
  in

  let l = List.length li in

  pair l li , impair l li

let test = separe [0;1;2;3]

(*b*)
(* let join (l1,l2) = 
  let rec j0 = function
    |[],[] -> []
    |li,[] -> li
    |h::t , li -> h:: j1 t li
    |_ -> failwith "cas imposible"
    and j1 = function
    |[],[] -> []
    |[],li -> li
    |li,h::t -> h :: j0 li t
    |_ -> failwith "cas imposible"
  in
  j0 l1,l2  *)
(* let rec join (l1,l2) =
  |[x],[y] -> [x;y]
  |[],li -> li
  |li,[] -> li
  |h::t,li -> h:: join li t *)

(* let rec join (l1,l2) = 
  |[],[] -> []
  |[x],[y] -> x::y
  |[x],[] -> [x]
  |[],[y] -> [y]
  |h::t,[] -> h::t
  |[], h::t -> h::t
  |a::b,c::d -> a::c:: join b d *)



