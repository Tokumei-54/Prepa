type point = float * float

let distance (xp,yp) (xq,yq) = sqrt ((xp -. xq)**2. +. (yp -. yq)**2.)

let distance_minimale t =
  let n = Array.length t in
  let min = ref (t.(0) , t.(1)) in
  let dmin = ref (distance t.(0) t.(1)) in
  for i = 0 to n-1 do 
    for j = i + 1 to n-1 do
      let d = distance t.(i) t.(j) in
      if d < !dmin then dmin := d ; min := (t.(i) , t.(j));
    done
  done;  !min,!dmin

let rec min_dist_div t = match Array.length t with
  |0|1|2 ->
  |n -> tx = 4