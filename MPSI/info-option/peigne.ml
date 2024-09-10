type arbre = F of int | N of arbre * arbre

(* 1. *)
let test_tree = N (N (N (N(F 5,F 4) ,F 3),F 2),F 1)

(* 2. *)
(* n-1 *)

(* 3. *)
let rec est_range = function
  |F _ -> true
  |N (g, F _ ) -> est_range g
  |N (_, _) -> false

let test3 =est_range test_tree

(* 4. *)
let rec est_peigne_stric = function
  |F _ -> true
  |N (g, F _ ) -> est_peigne_stric g
  |N (F _,  d ) -> est_peigne_stric d
  |N (_ , _) -> false

let est_peigne = function
  |F _ -> true
  |N (g ,d ) -> est_peigne_stric g &&  est_peigne_stric d

(* 5. *)
(* b *)
let rotation = function
  |
