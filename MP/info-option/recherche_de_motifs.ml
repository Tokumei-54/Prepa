let recherche_mot mot text =
  let n = String.length mot and m = String.length text in
  let occ = ref []
  for i = 0 to m - 1 do
    if text.[i] = mot.[0] then
      let w = String.sub text i n in 
      if w = mot then occ := i::!occ;
  done !occ

