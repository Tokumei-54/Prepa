type graphe = (int*int) list array

let rec insere p (a,b,w) = match p with
  | [] -> (a,b,w)::[]
  | (s1,s2,w12)::t -> if w <= w12 then (a,b,w)::p else (s1,s2,w12)::insere t (a,b,w)


let prime g = 
  let n = Array.length g in
  let v = Array.make n false in v.(0)  <- true;
  let e = Array.make n [] in
  let insert_all s p = List.fold_left (fun l (x,y) -> insere l (s,x,y)) p g.(s)  in
  let f = ref (insert_all 0 []) in 
  while not (Array.fold_left (&&) true v) do
    match !f with
    | [] -> failwith "aahhahahahaha"
    | (s1,s2,w)::t -> f:= t ; if not v.(s1) && v.(s2) then e.(s1) <- (s2,w)::e.(s1);
      if v.(s1) then (v.(s2) <- true; f:= insert_all s2 !f) else v.(s1) <- true; f:= insert_all s2 !f
  done; e


let g = [|[(1,2);(2,5);(3,8)];[(0,2);(3,9)];[(0,5);(4,1);(6,4)];[(0,8);(1,9);(5,7)];[(2,1);(5,6);(6,3)];[(3,7);(4,6)];[(2,4);(4,3)]|]
let test = prime g