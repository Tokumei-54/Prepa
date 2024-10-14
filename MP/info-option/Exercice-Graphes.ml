type sommet = int
type graphe = sommet list array

let graphe_vide (n:int) : graphe = Array.make n []

let ordre (g:graphe) : int = Array.length g

let test = ordre (graphe_vide 10)

let taille (g:graphe) : int = (Array.fold_left (+) 0 (Array.map (List.length) g))/2 

let test2 = taille (graphe_vide 10)

let voisinage (g:graphe) (s:sommet) = g.(s)

let exist_arete (g:graphe) (s1:sommet) (s2:sommet) = List.mem s2 g.(s1)

let ajoute (g:graphe) (s1:sommet) (s2:sommet) = 
  let rec inserer s = function
    |[] -> s::[]
    |h::t -> if s = h then h::t else if s < h then s::h::t else h::inserer s t
  in 
  g.(s1) <- inserer s2 g.(s1);
  g.(s2) <- inserer s1 g.(s2)

let supprimer (g:graphe) (s1:sommet) (s2:sommet) = 
  let rec suppr s = function
    |[] -> s::[]
    |h::t -> if s = h then t else h::suppr s t
  in 
  g.(s1) <- suppr s2 g.(s1);
  g.(s2) <- suppr s1 g.(s2)

(* let supprimer2 (g:graphe) (s1:sommet) (s2:sommet) = 
  let rec suppr x = List.filter (fun s -> s = x) in 
  g.(s1) <- suppr s2 g.(s1);
  g.(s2) <- suppr s1 g.(s2) *)

let rec iter f = function
  |[] -> ()
  |h::t -> f h ; iter f t

let iter_voisins (f:sommet -> unit) (g:graphe) (s:sommet) = iter f g.(s)  

let iter_aretes (f:sommet -> sommet -> unit) (g:graphe) = 
  for s = 0 to ordre g - 1 do
    iter_voisins (f s) g s ;
  done

let affiche_voisins (g:graphe) = iter_voisins print_int g 

let affiche_aretes = iter_aretes (fun s1 s2 -> Printf.printf "(%d , %d) \n" s1 s2)

let g_complet (n:int) = Array.init n (fun i -> List.init (n-1) (fun j ->  if j >= i then j+1 else j))

let test3 = g_complet 10
let test4 = affiche_aretes test3