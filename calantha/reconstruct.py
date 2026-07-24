import re, urllib.parse
# imginn src -> real cdninstagram url
def real(src):
    # format: https://sN.imginn.com/<FN>?<tprefix>/<FN>?<QUERY>
    m = re.match(r'https://s\d+\.imginn\.com/([^?]+)\?(t[\d.\-]+)/[^?]+\?(.*)$', src)
    if not m: return None
    fn, tprefix, query = m.groups()
    q = urllib.parse.parse_qs(query, keep_blank_values=True)
    host = q.get('_nc_ht',[None])[0]
    if not host: return None
    return f"https://{host}/v/{tprefix}/{fn}?{query}"

srcs = {
 "calantha-logo": "https://s3.imginn.com/724660506_18093570767595695_6414892208696696793_n.jpg?t51.82787-19/724660506_18093570767595695_6414892208696676793_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_cat=107&ccb=7-5&_nc_sid=f7ccc5&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMyIn0%3D&_nc_ohc=r3f2pfpYSa8Q7kNvwEyhx1l&_nc_oc=AdodKB7aKm7q6z1_qp-7zHetSgrEKon2aTxTJwXixYADU1Y6fc--tTTL4ujwIWBylp7vp52_Xb7aubg4n0IGxU3Y&_nc_zt=24&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=sKhnWCmW9ouCx4CJm5H5RA&_nc_ss=73689&oh=00_AQCEot-Z5U8jFsQz4-nT0qpt9csvHtPi2Q30N2buagN5rQ&oe=6A695811",
}
for name,s in srcs.items():
    print(name, "->", real(s))
