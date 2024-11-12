let grapheEX = [|
[|0  ;220;691;0  ;0  ;0  |];
[|220;0  ;463;583;677;0  |];
[|691;463;0  ;0  ;458;314|];
[|0  ;583;0  ;0  ;246;0  |];
[|0  ;677;458;246;0  ;405|];
[|0  ;0  ;314;0  ;405;0  |]
|]

(* 1 *)
let liste_aretes g = 
  let n = Array.length g in
  let m = Array.length g.(0) in
  let p = ref [] in
  for i = 0 to n-1 do
    for j = i+1 to m-1 do
      let w = g.(i).(j) in
      if w <> 0 then
        p := (i,j,w)::!p
      done
    done;
  !p


let liste_aretes_rec g = 
  let n = Array.length g in
  let m = Array.length g.(0) in
  let rec aux = function
    |(i,j) when i = n -> []
    |(i,j) when j = m -> aux (i+1,i+2)
    |(i,j) -> let w = g.(i).(j) in 
              if w <> 0 then (i,j,w) :: aux (i,j+1) else aux (i,j+1)
  in aux (0,1)

let test1 = liste_aretes grapheEX
let test2 = liste_aretes_rec grapheEX

let liste_aretes_triees g = 

  let rec fusion l1 l2 = match l1,l2 with
    |[],l|l,[] -> l
    |(i1,j1,w1)::t1,(i2,j2,w2)::t2 -> 
      if w1 <= w2 
      then (i1,j1,w1)::fusion t1 l2
      else (i2,j2,w2)::fusion l1 t2
  in

  let div = 
    let rec aux l1 l2 = function
      |[] -> l1,l2
      |h::[] -> h::l1,l2
      |h1::h2::t -> aux (h1::l1) (h2::l2) t
    in aux [] []  
  in

  let rec tri = function
    |[] -> []
    |x::[] -> x::[]
    |l -> let l1,l2 = div l in fusion (tri l1) (tri l2)
  in

  tri (liste_aretes_rec g) 

let test2 = liste_aretes_triees grapheEX

(* 3. les composantes connexes forment une partition de V donc soit u et v sont dans la même composante connexe et le cas (ii) se produit soit il ne le sont pas et on se trouve dans le cas (i) *)
(* 4. cf feuille *)
(* 5. on peut construire un tel arbe en enlevent des arrete jusqu'as devenir minimal conexe par exemple *)
(* 6. cf feuille*)
(* 7. la composante connexe qui contient le sommet 0 *)
(* 8. cf feuille *)
(* 9. cf feuille *)

let creer n = Array.init n (fun i -> i)
let rec composante c i = let j = c.(i) in if i = j then i else composante c j

let fusionner1 c i j = c.(j) = i
let fusionner2 c i j = c.(j) = composante c i


let tri_lineaire k t =
  let n = Array.length t in
  let o = Array.make k 0 in 
  for i=0 to n-1 do let j = t.(i) in o.(j) <- o.(j) + 1 done ;
  let p = ref 0 and q = ref 0 in
  while  !p < k do(
    if o.(!p) = 0 
      then incr p
    else o.(!p) <- o.(!p) - 1; t.(!q) <- !p; incr q)
  done




