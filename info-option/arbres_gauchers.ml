(* 1. *)
(*
2 non
2 non
1 oui
2 oui
*)

(* 2. *)
type 'a arbre = Vide | N of 'a * 'a arbre * 'a arbre
let test_tree = N (6,N (4,Vide,Vide),N (5,N(2,N(1,Vide,Vide),Vide),Vide))
let rang =
  let rec aux acc = function
    |Vide -> acc
    |N (_,_,d) -> aux (succ acc) d
  in aux 0

let test1 = rang test_tree

(* 3. *)
let gaucher =
  let rec aux p = function
    |Vide -> true 
    |N (n,g,d) -> p > n && rang g >= rang d && aux n g && aux n d
  in function
  |Vide -> true
  |N (n,g,d) -> rang g >= rang d && aux n g && aux n d

let test2 = gaucher test_tree

(* 4. *)
(* 0 <= rg(a) <= log2(|a| +1) *)

type 'a arbre = Vide | N of int * 'a * 'a arbre * 'a arbre
let test_tree1 = N (2,6,N (1,4,Vide,Vide),N (1,5,N(1,2,N(1,1,Vide,Vide),Vide),Vide))
let test_tree2 = N (1,5,N(1,3,N(1,2,N(1,1,N(1,0,Vide,Vide),Vide),Vide),Vide),Vide)
(* 5. *)
let rang = function
  |Vide -> 0
  |N (i,_,_,_) -> i

(* 6. *)
let rec fusion a b = match a,b with
  |Vide,Vide -> Vide
  |c,Vide|Vide,c -> c
  |N (i,n,g1,d1),N (j,m,g2,d2) -> if n > m then (let f = fusion d1 (N (j,m,g2,d2)) in if i > j then N (i,n,g1,f) else N (j,n,f,g1) )
                                  else  (let f = fusion d2 (N (i,n,g1,d1)) in if j > i then N (j,m,g2,f) else N (i,m,f,g2) )

let test6 = fusion test_tree1 test_tree2

(* 7. *)
let rec insertion e = function
  |Vide -> N (1,e,Vide,Vide)
  |N (i,n,g,d) -> if e > n then N (1,e,N(i,n,g,d),Vide) else N (i,n,insertion e g,d)

(* 8. *)
let extraire_max = function
  |Vide -> failwith "arbre vide"
  |N (_,m,g,d) -> m,fusion g d

(* 9. *)