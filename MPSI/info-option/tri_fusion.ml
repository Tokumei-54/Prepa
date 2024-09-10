let partage =
  let rec aux acc1 acc2 = function
    |[] -> acc1, acc2
    |h::t -> aux acc2 (h::acc1) t
  in aux [] [] 

let test1 = partage [2;3;5;7;4;8;1;6;9]

let rec fusion l1 l2 = match l1, l2 with
  | l,[] |[],l -> l
  |h1::t1 , h2::t2 -> if h1 <= h2 then h1::fusion t1 l2 else h2::fusion l1 t2

let test2 = fusion [1;3;5;7;9] [2;4;6;8]

let rec tri_fusion = function
  |[] -> []
  |[v] -> [v]
  |l -> let l1, l2 = partage l in fusion (tri_fusion l1) (tri_fusion l2) 

  let test3 = tri_fusion [2;3;5;7;4;8;1;6;9]

let fusion_t t1 t2 g m d = 
  let i = ref g in let j = ref m in let k = ref g in
  while !i <> m && !j <> d + 1 do
    (if t1.(!i) <= t1.(!j) then (t2.(!k) <- t1.(!i);incr i) else(t2.(!k) <- t1.(!j);incr j); incr k)
    done;
  if !i <> m then for l = !i to m - 1 do t2.(!k + l - !i) <- t1.(l) done;
  if !j <> d + 1 then for l = !j to d do t2.(!k + l - !j) <- t1.(l) done
  
let t1 = [|1;3;5;7;9;0;2;4;6;8|]
let t2 = [|-1;-1;-1;-1;-1;-1;-1;-1;-1;-1|]

let test4 = fusion_t t1 t2 0 5 9

let tri_fusion_t tab = 
  let copy = Array.copy tab in
  let rec aux i j = function()
    |  