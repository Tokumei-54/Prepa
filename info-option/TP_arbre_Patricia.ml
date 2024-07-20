type mot = char list
type dico = (mot * int) list

let string_to_char_list ch = List.init (String.length ch) (String.get ch)
let truc (ch , i) = (string_to_char_list ch , i)
let dico_test = List.map truc [("1",1);("12",2);("123",3)]
(* 1. l'ajout de couple clef valeurs *)

(* 2. *)
let plus_long d =
  let rec aux max maxm = function
    | [] -> maxm
    | (m , i) :: t -> let l = List.length m in if l > max then aux l m t else aux max maxm t
  in aux 0 [] d

let test2 = plus_long dico_test

(*3.*)
let rec prefixe u v = match u,v with
  | _,[] -> false
  | [], _ -> true
  | h1::t1,h2::t2 -> h1 = h2 && prefixe t1 t2

let test3 = prefixe (string_to_char_list "pre") (string_to_char_list "prefixe")

(* 4. *)
let egaux u v = u = v

(* 5. *)
let rec recherche m = function
  | [] -> -1
  | (n , i) :: t ->  if n = m then i else recherche m t

let test5 = recherche (string_to_char_list "12") dico_test 

(* 6. bah ça marche*)

(* 7. *)

(* 8. *)
let rec suppression m = function
  | [] -> [] 
  | (n , i) :: t ->  if n = m then t else  (n , i) :: suppression m t

  let test8 = suppression (string_to_char_list "12") dico_test 

type patricia = N of mot * int * patricia list
let test_patricia = N ( [], -1, [N ( ['a';'s'], 1, []) ; N ( ['f';'a'], 2, [N ( ['b';'l';'e'], 3, []) ; N (['c'], -1, [N (['e'], 4, []) ; N (['i';'l';'e'],5,[])])] ); N (['l'],-1, [N (['a'],6,[]) ; N (['e'], 7, [])])])

(* 9. *)
let rec taille acc = function
  |N ([] , -1 , []) -> acc
  |N ( _ , _ , []) -> acc + 1
  |N (_ , -1 , p) -> List.fold_left taille acc p
  |N ( _ , _ , p) -> List.fold_left taille (succ acc) p

let test9 = taille 0 test_patricia

(* 10. *)
let rec prefixage m = function
  | [] -> [] 
  | (n , i) :: t -> (m @ n , i)::prefixage m t

(* 11. *)
let rec concat acc = function
  |[] -> acc
  |h::t -> concat (acc @ h) t

let rec dico_patricia = function
  |N ([], -1, []) -> []
  |N (m, i, []) -> (m, i)::[]
  |N (m, -1, p) -> prefixage m  (concat [] (List.map dico_patricia p))
  |N (m, i, p) -> (m , i) :: prefixage m  (concat [] (List.map dico_patricia p))

let test11 = dico_patricia test_patricia

(* 12. *)
let compare m n = match m,n with
  |[],[] |[],_ |_,[] -> failwith "liste vide"
  |((a,_)::_),((b,_)::_) -> a < b

(* 13. *)

