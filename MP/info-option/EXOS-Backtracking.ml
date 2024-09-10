(* Exercice 3.1 *)
(* a *)
let rec exist_subset s = function
  |[] -> s = 0
  |h::t ->  exist_subset (s - h) t  || exist_subset s t

let test = exist_subset 10 [0;1;2;3;4;5;6;7;8;9]

(* b *)
let sum = List.fold_left (+) 0
let add x = List.map(fun l -> x::l)


let subset s a= 
  let rec aux n l= 
  (* if n < 0 then [[]] else *)
  match l with
    |[] -> [[]]
    |h::t -> add h (aux (n-h) t) @ aux n t
  in List.filter (fun e -> sum e = s ) (aux s a)

let test2 = subset 10 [0;1;2;3;4;5;6;7;8;9]

