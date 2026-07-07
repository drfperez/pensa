import ast
from errors import PensaError

class Interpreter:
    def __init__(self):
        self.vars={}; self.funcs={}
    def val(self,t):
        t=t.strip()
        if t in self.vars: return self.vars[t]
        if t.startswith('['): return ast.literal_eval(t)
        if t.startswith('"') and t.endswith('"'): return t[1:-1]
        try: return int(t)
        except: return t
    def cond(self,c):
        expr=c
        for k,v in sorted(self.vars.items(), key=lambda x:-len(x[0])):
            expr=expr.replace(k,repr(v))
        expr=expr.replace(' i ',' and ').replace(' o ',' or ')
        return bool(eval(expr,{"__builtins__":{}},{}))
    def block(self,lines):
        i=0
        while i<len(lines):
            s=lines[i].strip()
            if not s or s.startswith('#'): i+=1; continue
            if s.startswith('mostra '): print(self.val(s[7:]))
            elif s.startswith('guarda '):
                a,b=s[7:].split(' dins ',1); self.vars[b.strip()]=self.val(a)
            elif s.startswith('suma '):
                a,b=s[5:].split(' a ',1); self.vars[b.strip()]+=self.val(a)
            elif s.startswith('resta '):
                a,b=s[6:].split(' a ',1); self.vars[b.strip()]-=self.val(a)
            elif s.startswith('funcio '):
                nom=s[7:].strip(); blk=[]; i+=1; d=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('funcio '): d+=1
                    if t=='acaba': d-=1
                    if d==0: break
                    blk.append(lines[i]); i+=1
                self.funcs[nom]=blk
            elif s.startswith('crida '):
                self.block(self.funcs[s[6:].strip()])
            elif s.startswith('si '):
                c=s[3:]; yes=[]; no=[]; cur=yes; i+=1; d=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('si '): d+=1
                    if t=='acaba': d-=1
                    if d==0: break
                    if d==1 and t=='si no': cur=no; i+=1; continue
                    cur.append(lines[i]); i+=1
                self.block(yes if self.cond(c) else no)
            elif s.startswith('mentre '):
                c=s[7:]; blk=[]; i+=1; d=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('mentre '): d+=1
                    if t=='acaba': d-=1
                    if d==0: break
                    blk.append(lines[i]); i+=1
                while self.cond(c): self.block(blk)
            elif s.startswith('repeteix '):
                n=int(s.replace('repeteix ','').replace(' vegades','')); blk=[]; i+=1; d=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('repeteix '): d+=1
                    if t=='acaba': d-=1
                    if d==0: break
                    blk.append(lines[i]); i+=1
                for _ in range(n): self.block(blk)
            elif s.startswith('per cada '):
                r=s[9:]; var,ll=r.split(' dins ',1); blk=[]; i+=1; d=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('per cada '): d+=1
                    if t=='acaba': d-=1
                    if d==0: break
                    blk.append(lines[i]); i+=1
                for e in self.vars.get(ll.strip(),[]):
                    self.vars[var.strip()]=e; self.block(blk)
            else: raise PensaError(f'Instrucció desconeguda: {s}')
            i+=1
