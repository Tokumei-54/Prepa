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
  | N (g,x,d) -> let hg = hauteur g and hd = hauteur d in (hg = hd || hg = hd + 1 || hg = hd -1) && is_equilibre g && is_equilibre d

