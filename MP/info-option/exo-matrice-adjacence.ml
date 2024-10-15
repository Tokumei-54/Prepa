type sommet = int
type graphe = bool array array

let graphe_vide (n:int) : graphe = Array.make_matrix n n false

let ordre (g: graphe): int = Array.length g

let taille (g: graphe): int = Array.fold_left (fun acc1 g -> Array.fold_left (fun acc2 b -> if b then acc2 + 1 else acc2) 0 g + acc1) 0 g

let existe_arc (g: graphe) (x:sommet) (y:sommet) : bool = g.(x).(y)

let ajoute_arc (g: graphe) (x:sommet) (y:sommet) : unit = g.(x).(y) <- true

let supprime_arc (g: graphe) (x:sommet) (y:sommet) : unit = g.(x).(y) <- false

let voisinage (g: graphe) (x:sommet) : sommet list = 
  let n = ordre g in 
  let rec aux = function
    |i when i = n -> []
    |i -> if g.(x).(i) then i::aux (i+1) else aux (i+1)
  in aux 0


let g = graphe_vide 3
let test = g.(0).(0) <- true; 7

let iter_voisins (f:sommet -> unit) (g: graphe) (x:sommet) :unit= List.iter f (voisinage g x)

let iter_arcs (f:sommet -> sommet-> unit) (g: graphe) :unit = 
  for i = 0 to ordre g - 1 do
    iter_voisins (f i) g i;
  done

let affiche_voisins (g: graphe) (x:sommet) :unit = iter_voisins (fun i -> Printf.printf "%d" i) g x

let test2 = affiche_voisins g 0

let affiche_arcs (g: graphe) :unit = iter_arcs (fun i j -> Printf.printf " %d-%d \n" i j) g

let test3 = affiche_arcs g

let g_complet (n:int) : graphe = Array.make_matrix n n true

let retourne_arcs (g: graphe) :unit = 
  for i = 0 to ordre g - 1 do
    for j = 0 to i - 1 do 
      let tmp = g.(i).(j) in
      g.(i).(j) <- g.(j).(i);
      g.(j).(i) <- tmp;
    done
  done

let c = graphe_vide 3
let test4 = c.(0).(1) <- true; c.(1).(2) <- true;Printf.printf " --- \n" ;affiche_arcs c;Printf.printf " --- \n" ;retourne_arcs c; affiche_arcs c;Printf.printf " --- \n" 

let desoriente (g: graphe) :unit = 
  for i = 0 to ordre g -1 do
    for j = 0 to i-1 do 
      if g.(i).(j) then g.(j).(i) <- true else  g.(i).(j) <- g.(j).(i) 
    done
  done

let chemin (g: graphe) =
  let rec aux s = function
    |[] -> true
    |h::t -> g.(s).(h) && aux h t
  in function
    |[] -> true
    |hd::tl -> aux hd tl 

let affiche_matrice m = 
  let n = Array.length m -1 in
  let p = Array.length m.(0) -1 in
  Printf.printf "\n";
  for i = 0 to n do
    Printf.printf "(";
    for j = 0 to p do
      Printf.printf " %d " m.(i).(j)
    done;
    Printf.printf ")";
  done

let iter_matrix f m = 
  let n = Array.length m -1 in
  let p = Array.length m.(0) -1 in
  for i = 0 to n do
    for j = 0 to p do
      f m.(i).(j)
    done;
  done

let matrix_of_graph = map_matrix (fun b -> if b then 1 else 0)  

let test5 = affiche_matrice (matrix_of_graph c)