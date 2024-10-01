type 'a tas = V | N of 'a tas * 'a * 'a tas

let est_vide t = t = V

let lire = function
  | V -> failwith "tas vide"
  | N(_,a,_) -> a

let rec hauteur = function
  | V -> 0
  | N(g,_,d) -> 1 + max (hauteur g)  (hauteur d)
let rec est_tdb = function
  | V | N(V,_,V) -> true 
  | N(V,a,N(V,b,V)) | N(N(V,b,V),a,V)-> a <= b
  | N(g,a,d) -> a <= lire g && a <= lire d && (let hd = hauteur d and hg = hauteur g in hd <= g || hg <= hd + 1) && est_tdb g && est_tdb d


let rec inserer x = function
  | V -> N(V,x,V)
  | N(g,y,d) when x < y -> if hauteur g >= hauteur d then N(g,x , inserer y d) else N(inserer y g, y, d)
  | N(g,y,d) -> if hauteur g >= hauteur d then N(g,y, inserer x d) else N(inserer x g, y, d)
   

