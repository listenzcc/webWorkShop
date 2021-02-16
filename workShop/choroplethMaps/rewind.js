// Rewind the geoJson object to clockwise or anti-clockwise
// It will 'correct' the order of the vertex of multi-polygon in features
// ! For D3.js library
// Usage example: geojsonRewind(geoJson, true)

!(function (e) {
  if ("object" == typeof exports && "undefined" != typeof module)
    module.exports = e();
  else if ("function" == typeof define && define.amd) define([], e);
  else {
    ("undefined" != typeof window
      ? window
      : "undefined" != typeof global
      ? global
      : "undefined" != typeof self
      ? self
      : this
    ).geojsonRewind = e();
  }
})(function () {
  return (function () {
    return function e(n, t, r) {
      function o(u, f) {
        if (!t[u]) {
          if (!n[u]) {
            var a = "function" == typeof require && require;
            if (!f && a) return a(u, !0);
            if (i) return i(u, !0);
            var s = new Error("Cannot find module '" + u + "'");
            throw ((s.code = "MODULE_NOT_FOUND"), s);
          }
          var c = (t[u] = { exports: {} });
          n[u][0].call(
            c.exports,
            function (e) {
              return o(n[u][1][e] || e);
            },
            c,
            c.exports,
            e,
            n,
            t,
            r
          );
        }
        return t[u].exports;
      }
      for (
        var i = "function" == typeof require && require, u = 0;
        u < r.length;
        u++
      )
        o(r[u]);
      return o;
    };
  })()(
    {
      1: [
        function (e, n, t) {
          var r = e("@mapbox/geojson-area");
          function o(e, n) {
            return function (t) {
              return e(t, n);
            };
          }
          function i(e, n) {
            (n = !!n), (e[0] = u(e[0], n));
            for (var t = 1; t < e.length; t++) e[t] = u(e[t], !n);
            return e;
          }
          function u(e, n) {
            return (function (e) {
              return r.ring(e) >= 0;
            })(e) === n
              ? e
              : e.reverse();
          }
          n.exports = function e(n, t) {
            switch ((n && n.type) || null) {
              case "FeatureCollection":
                return (n.features = n.features.map(o(e, t))), n;
              case "Feature":
                return (n.geometry = e(n.geometry, t)), n;
              case "Polygon":
              case "MultiPolygon":
                return (function (e, n) {
                  "Polygon" === e.type
                    ? (e.coordinates = i(e.coordinates, n))
                    : "MultiPolygon" === e.type &&
                      (e.coordinates = e.coordinates.map(o(i, n)));
                  return e;
                })(n, t);
              default:
                return n;
            }
          };
        },
        { "@mapbox/geojson-area": 2 },
      ],
      2: [
        function (e, n, t) {
          var r = e("wgs84");
          function o(e) {
            var n = 0;
            if (e && e.length > 0) {
              n += Math.abs(i(e[0]));
              for (var t = 1; t < e.length; t++) n -= Math.abs(i(e[t]));
            }
            return n;
          }
          function i(e) {
            var n,
              t,
              o,
              i,
              f,
              a,
              s = 0,
              c = e.length;
            if (c > 2) {
              for (a = 0; a < c; a++)
                a === c - 2
                  ? ((o = c - 2), (i = c - 1), (f = 0))
                  : a === c - 1
                  ? ((o = c - 1), (i = 0), (f = 1))
                  : ((o = a), (i = a + 1), (f = a + 2)),
                  (n = e[o]),
                  (t = e[i]),
                  (s += (u(e[f][0]) - u(n[0])) * Math.sin(u(t[1])));
              s = (s * r.RADIUS * r.RADIUS) / 2;
            }
            return s;
          }
          function u(e) {
            return (e * Math.PI) / 180;
          }
          (n.exports.geometry = function e(n) {
            var t,
              r = 0;
            switch (n.type) {
              case "Polygon":
                return o(n.coordinates);
              case "MultiPolygon":
                for (t = 0; t < n.coordinates.length; t++)
                  r += o(n.coordinates[t]);
                return r;
              case "Point":
              case "MultiPoint":
              case "LineString":
              case "MultiLineString":
                return 0;
              case "GeometryCollection":
                for (t = 0; t < n.geometries.length; t++)
                  r += e(n.geometries[t]);
                return r;
            }
          }),
            (n.exports.ring = i);
        },
        { wgs84: 3 },
      ],
      3: [
        function (e, n, t) {
          (n.exports.RADIUS = 6378137),
            (n.exports.FLATTENING = 1 / 298.257223563),
            (n.exports.POLAR_RADIUS = 6356752.3142);
        },
        {},
      ],
    },
    {},
    [1]
  )(1);
});
