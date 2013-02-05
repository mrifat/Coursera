import java.util.list;
import java.util.ArrayList;
public class UF{

  public UF(int N){
    List<int[]> component_arrays = new ArrayList<int[]>(N);
    fill_arrays(N);
  }

  void fill_array(int N){
    for(int i=0; i<N; i++){
      component_arrays[i][0] = i;
    }

  }

  void union(int p, int q){
    int q_index;
    if(!is_connected()){
      if(component_arrays[p].contains(p)){
        component_arrays[p].add(component_arrays[component_arrays.indexOf(q)]);
        component_arrays.remove(component_arrays.indexOf(q));
        component_arrays.trimToSize();
      }
    }
  }
}
