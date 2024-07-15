// 1
let head = {
    glasses: 1
  };
  
  let table = {
    pen: 3
  };
  
  let bed = {
    sheet: 1,
    pillow: 2
  };
  
  let pockets = {
    money: 2000
  };

  Object.setPrototypeOf(pockets, bed);
  Object.setPrototypeOf(bed, table);
  Object.setPrototypeOf(table, head);

  Object.getPrototypeOf(pockets);

  // 2
  // It is easier to get head.glasses because it only has the check the 
  // last prototype in the chain (well second to last). pocket.glasses on the other hand
  // first checks pockets, then bed, then table, then head