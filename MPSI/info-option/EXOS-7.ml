(*Exercice 7.1*)

(*a*)
let rec mul = function
  |[] -> 1
  |0::t -> 0
  |h::t -> h * mul t

let test = mul [1;2;3]

(*c*)
let rec mul2 acc = function
  |[] -> acc
  |0::t -> 0
  |h::t -> mul2 (acc * h) t


let test = mul2 1 [1;2;3] 

(*Exercice 7.2*)

(*a*)
let rec list_of_string = function
  |"" -> []
  |ch -> ch.[0]::list_of_string (String.sub ch 1 (String.length ch -1))

let test = list_of_string "test"

(*b*)
let rec string_of_list = function
  |[] -> ""
  |h::t -> String.make 1 h ^ string_of_list t

let test = string_of_list ['t'; 'e'; 's'; 't']

(*Exercice 7.3*)

(*a*)

let rec enleve li n = match li with
  | [] -> []
  |h::t -> match n with
    | 0 -> li
    | _ -> enleve t (pred n)

    let test = enleve [1;2;3] 2

(*b*)
let rec premiers li n = 
  match li with
  | [] -> []
  |h::t -> match n with
    | 0 -> []
    | _ -> h::premiers t (pred n)

let test = premiers [1;2;3;4;5] 3

(*c*)

let tranche li i j = premiers (enleve li i) (j-i + 1)

let test = tranche [1;2;3;4;5] 1 3

(*d*)
let decoupe li p = 
  let rec f n = function
    |[] -> []
    |h::t -> if n = 0 then h::f ((succ n) mod p) t else f ((succ n) mod p) t
  in
  f 0 li

let test = decoupe [1;2;3;4;5] 2

(*e*)

let slice li i j p = decoupe (tranche li i j) p

let test = slice [0;1;2;3;4;5;6;7;8;9] 4 9 2

(*Exercice 7.4*)

(*a*)
let rec map f = function
  |[] -> []
  |h :: t -> f h :: map f t

let test = map (function | x -> 2 * x) [0;1;2;3;4;5;6;7;8;9]

(*b*)
let rec filter f = function
  |[] -> []
  |h :: t -> if f h then h :: filter f t else filter f t

let test = filter (function | x -> x mod 2 = 0) [0;1;2;3;4;5;6;7;8;9]