type 'a arbre = V | N of 'a arbre *'a * 'a arbre
let test_tree = N (N (N(V,4,V),2,V), 1, N (N(V,5,V),3,N(V,6,V)))


let rec taille = function
  |V -> 0
  |N (g,_,d) -> 1 + taille g + taille d

let rec hauteur = function
  |V -> -1
  |N (g,_,d) -> 1 + max (hauteur g)  (hauteur d)

let rec nfeuille = function
  |V -> 0
  |N (V,_,V) -> 1
  |N (g,_,d) -> nfeuille g + nfeuille d

let rec is_entier = function
  |V -> false
  |N (V,_,V) -> true
  |N (g,_,d) -> is_entier g && is_entier d

let testa = taille test_tree
let testb = hauteur test_tree
let testc = nfeuille test_tree
let testd = is_entier test_tree

let rec in_tree n = function 
  |V -> false
  |N (g,x,d) -> x = n || in_tree n g || in_tree n d

let rec chemin n = function 
  |V -> []
  |N (g,x,d) -> if in_tree n g then x::chemin n g else x::chemin n d

let rec nb_noeud_prof k n = function 
  | V -> 0
  | N (g,_,d) -> if n = k then 1 else let m = succ n in nb_noeud_prof k m g + nb_noeud_prof k m d

let testa = in_tree 4 test_tree
let testb = chemin 5 test_tree
let testc = nb_noeud_prof 2 0 test_tree

let rec feuilles = function
  | V -> []
  | N (V,x,V) -> [x]
  | N (g,x,d) -> feuilles g @ feuilles d

let rec is_equilibre = function
  | V -> true
  | N (g,x,d) -> abs (hauteur g - hauteur d) <= 1 && is_equilibre g && is_equilibre d

let testa = feuilles test_tree
let testb = is_equilibre test_tree

let rec symetrique = function
  |V -> V
  |N (g,x,d) -> N (symetrique d, x, symetrique g)

(* let rec parcour = function
  |V -> [-1]
  |N (g,x,d) -> parcour g @ x::parcour d  *)
(* let rec alt l1 l2 = match l1,l2 with
  |[],[] -> []
  |[],l2 -> l2
  |l1,[] -> l1
  |h1::t1,h2::t2 -> h1::h2::alt t1 t2


let rec parcour = function
|V -> [-1]
|N (g,x,d) -> x:: alt (parcour g) (parcour d) 

let rec tree_of_list = function
  |[] -> V
  |h::t -> N () *)


let testa = symetrique test_tree
(* let testb = parcour test_tree *)