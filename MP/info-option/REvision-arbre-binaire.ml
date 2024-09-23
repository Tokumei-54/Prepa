type 'a arbre = V | N of 'a arbre * 'a * 'a arbre

(* Exercice 1.1 *)
(* a. t(p) = 1 + t(f1)+ t(f2))  h(p) = 1+max(h(f1),h(f2))  f(a) =  *)

let rec taille = function
  | V -> 0
  | N(V,_,V) -> 1
  | N(g,_,d) -> 1 + taille g + taille d


let rec hauteur = function
  | V -> 0
  | N(V,_,V) -> 1
  | N(g,_,d) -> 1 + max (hauteur g)  (hauteur d)

let rec feuille = function
  | V -> 0
  | N(V,_,V) -> 1
  | N(g,_,d) -> feuille g + feuille d

let rec entier = 