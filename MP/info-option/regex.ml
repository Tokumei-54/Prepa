type 'a regex = 
  | Vide
  | Epsilon
  | S of 'a
  | U of ('a regex * 'a regex)
  | C of ('a regex * 'a regex)
  | E of 'a regex

(* a *)
let test_regex = U(C(S 'a',E(S 'b')),E(U( S 'a',S 'b'))) 

(* b *)
let decomposition ch = let n = String.length ch in
  ("",ch)::(ch,""):: List.init (n-1) (fun i -> (String.sub ch 0 (i+1),String.sub ch (i+1) (n - i - 1)))


let rec test ch = function 
  | Vide -> false
  | Epsilon -> ch = ""
  | S s -> String.length ch = 1 && ch.[0] = s
  | U ( r1, r2) -> test ch r1 || test ch r2
  | C ( r1, r2) -> List.exists (fun (s1,s2) -> test s1 r1 && test s2 r2) (decomposition ch)
  | E r -> ch = "" || List.exists (fun (s1,s2) -> test s1 r && test s2 (E r)) (decomposition ch)

let t1 = test "" test_regex
let t2 = test "a" test_regex
let t3 = test "abbbb" test_regex
let t4 = test "babababab" test_regex
let t5 = test "bababacab" test_regex