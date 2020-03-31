import './main.scss'
import './css.css'

import {range, interval, fromEvent, of} from 'rxjs';
import {map, filter, take, scan, throttleTime, takeUntil, concatAll, skip,zip} from 'rxjs/operators';



let source = interval(500).pipe(
    take(3),
    zip(newest,(x,y)=>x+y)
).subscribe((v)=>console.log(v));
let newest = interval(300).pipe(
    take(3)
);

let source = interval(300);
let source2 = interval(1000);
source.pipe(
    buffer(source2)
).subscribe({
    next: (value) => { console.log(value); },
    error: (err) => { console.log('Error: ' + err); },
    complete: () => { console.log('complete'); }
})

