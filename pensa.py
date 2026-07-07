
class ReturnValue(Exception):
    def __init__(self,value):
        self.value=value

class Pensa:
    def __init__(self):
        self.vars={}
        self.funcs={}

    def val(self,t):
        t=t.strip()
        if t in self.vars: return self.vars[t]
        if t.startswith('"') and t.endswith('"'): return t[1:-1]
        try: return int(t)
        except: return t

    def eval_expr(self,expr):
        for k,v in sorted(self.vars.items(), key=lambda x:-len(x[0])):
            expr=expr.replace(k,repr(v))
        return eval(expr,{"__builtins__":{}},{})

    def call_func(self,name,args):
        if name not in self.funcs:
            raise Exception(f'Funció inexistent: {name}')
        params,body=self.funcs[name]
        if len(args)!=len(params):
            raise Exception(f'La funció {name} necessita {len(params)} paràmetres.')
        backup=dict(self.vars)
        for p,a in zip(params,args):
            self.vars[p]=a
        try:
            self.block(body)
            result=None
        except ReturnValue as r:
            result=r.value
        self.vars=backup
        return result

    def block(self,lines):
        i=0
        while i<len(lines):
            s=lines[i].strip()
            if not s or s.startswith('#'):
                i+=1; continue
            if s.startswith('mostra '):
                print(self.val(s[7:]))
            elif s.startswith('guarda crida '):
                rest=s[13:]
                head,var=rest.split(' dins ',1)
                parts=head.split()
                self.vars[var.strip()]=self.call_func(parts[0],[self.val(x) for x in parts[1:]])
            elif s.startswith('guarda '):
                a,b=s[7:].split(' dins ',1)
                self.vars[b.strip()]=self.val(a)
            elif s.startswith('retorna '):
                raise ReturnValue(self.eval_expr(s[8:]))
            elif s.startswith('funcio '):
                parts=s.split()
                name=parts[1]
                params=parts[2:]
                body=[]; i+=1; depth=1
                while i<len(lines):
                    t=lines[i].strip()
                    if t.startswith('funcio '): depth+=1
                    if t=='acaba':
                        depth-=1
                        if depth==0: break
                    body.append(lines[i]); i+=1
                self.funcs[name]=(params,body)
            elif s.startswith('crida '):
                parts=s.split()
                self.call_func(parts[1],[self.val(x) for x in parts[2:]])
            i+=1

if __name__=='__main__':
    import sys
    with open(sys.argv[1],encoding='utf-8') as f:
        Pensa().block(f.read().splitlines())
