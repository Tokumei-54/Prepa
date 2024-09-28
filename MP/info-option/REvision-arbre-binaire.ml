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

let rec entier = function
  | V -> false
  | N(V,_,V) -> true
  | N(g,_,d) -> entier g && entier d


(* Exercice 1.2 *)
(* a. parfait(p) = parfait(g) && parfait(d) *)

type squelette = SV | SN of squelette * squelette

let rec sph = function
  | 0 -> SV
  | h -> SN (sph (h-1) , sph (h-1))

(* let rec spn = function
  | 0 -> SV
  | n -> let q,r = n/2 , n mod 2 in SN (spn (q + r), spn(q)) *)

let spn n =
  let h = log (float_of_int n) /. log 2. in 
  let k = int_of_float h in
  if h = float_of_int k then sph k else failwith " pas entier"



let rec parfait = function 
  | SV |SN (SV,SV)-> true
  | SN (SV,_) | SN (_,SV) -> false
  | SN (g,d) -> parfait g && parfait d


let rec AVL = function
  | SV -> true
  | SN (g,d) -> 