let recherche_mot mot text =
  let n = String.length mot and m = String.length text in
  let occ = ref [] in
  for i = 0 to m - n do
    if text.[i] = mot.[0] then
      if String.sub text i n = mot then occ := i::!occ;
  done; !occ

let test1 = recherche_mot "test" "0testest000test00"

let div3 n =
  let l = String.length n in
  let s = ref 0 in
  for i = 0 to l-1 do
    if n.[i] = '1' then
      if i mod 2 = 0 then incr s else decr s;
  done; !s mod 3 = 0

let test2 = div3 "1100"

let palindrome ch = 
  let n = String.length ch and i = ref 0 in
  while ch.[!i] = ch.[n - !i-1] && !i <= n / 2 do
    incr i
  done; !i = n / 2 + 1

let test3 = palindrome "tenet"

let tranches n text =
  let m = String.length text in
  let occ = ref [] in
  for i = 0 to m - n do
    if palindrome (String.sub text i n) then occ := i::!occ;
  done; !occ

let voyelle = function
  | 'a' -> 0
  | 'e' -> 1
  | 'i' -> 2
  | 'o' -> 3
  | 'u' -> 4
  | 'y' -> 5
  |  _  -> 6

