from src.grammar.cnf_grammar import CnfGrammar
from src.graph.label_graph import LabelGraph
from src.utils.time_profiler import SimpleTimer
from src.algo.matrix_base import matrix_base_algo
from src.algo.single_source.single_source import SingleSourceAlgoBrute, SingleSourceAlgoSmart

g = LabelGraph.from_txt('deps/CFPQ_Data/data/WorstCase/Matrices/worstcase_128.txt')
gr = CnfGrammar.from_cnf('deps/CFPQ_Data/data/WorstCase/Grammars/Brackets.cnf')

with SimpleTimer():
    m = matrix_base_algo(g, gr)

ss_ab = SingleSourceAlgoBrute(g, gr)
sources_vertices = range(128)

with SimpleTimer():
    m1 = ss_ab.solve(sources_vertices)

ss_as = SingleSourceAlgoSmart(g, gr)

sum = 0
for i in sources_vertices:
    st = SimpleTimer()
    st.tic()
    m2 = ss_as.solve([i])
    st.toc()
    sum += st.duration

print(sum)

assert m[gr.start_nonterm].to_lists() == m1.to_lists(), 'Not equal!'
assert m[gr.start_nonterm].to_lists() == m2.to_lists(), 'Not equal!'