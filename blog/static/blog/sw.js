// version
var appVersion = "v1.0.0";

//fileto be cached
var files = [
  "/index.html",
  //"/css/style.css",
  //"/manifest.webmanifest",

];

//install
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(appVersion)
      .then((cache) => {
        return cache.addAll(files).catch((err) => {
          console.log("error while adding files in cache");
        });
      })
      .catch((err) => {
        console.log("error while opening caches", err);
      })
  );
  console.log("sw installed ");
  self.skipWaiting(); // this will not wait 
});

// Active
self.addEventListener("active", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        caches.map((cache) => {
          if (cache !== appVersion) {
            console.info("deleting old caches");
            return caches.delete(cache);
          }
        })
      );
    })
  );
  return self.clients.claim();
});
//fetch
self.addEventListener("fetch", (event) => {
  console.log("sw fetched");
  event.respondWith(
    fetch(event.request).then((res) => {
      if (res) {
        console.log(`fetch status : ${res}`)
        if (res.status == 200 ) {
          caches.open(appVersion)
            .then(function (cache) {
              return cache.add(event.request).catch(()=>{console.log("error")});
            });
          return res;
        } else {
          return caches.match("/404.html");
        }
      }
    }).catch(() => {
      return caches.match(event.request).then((res)=>{
        if(res.status == 200){
          return res;
        }
        return caches.match("/404.html");
      })
    })
  );
});
//backup
self.addEventListener("fetch1", (event) => {
  console.log("sw fetched");
  event.respondWith(
    caches.match(event.request).then((res) => {
      if (res) {
        console.log(`fetch status : ${res.status}`)
        if (res.status == 200) {
          return res;
        } else {
          return caches.match("/404.html");
        }
      }
      return fetch(event.request).catch(() => caches.match("/404.html"));
    })
  );
});
