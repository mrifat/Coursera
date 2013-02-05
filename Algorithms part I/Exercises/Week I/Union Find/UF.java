import java.util.List;
import java.util.ArrayList;
public class UF{
private List<int[]> component_arrays;
  public UF(int N){
    component_arrays = new ArrayList<int[]>(N);
    fill_arrays(N);
  }
  
  private void fill_arrays(int n) {
	  int[] x;
	  for(int i=0; i<n; i++){
		  component_arrays.add(new int[1]);
		  x = component_arrays.get(i);
		  for(int j=0; j<1;j++){
			  x[j] = i;
		  }
		  
	  }
	  
  }
  
  void union(int p, int q){
	  if(!is_connected(p, q)){
		 int p_index = find(p);
		 int q_index = find(q);
		 if(p_index != -1 && q_index != -1){
			 int[] p_array = component_arrays.get(p_index);
			 int[] q_array = component_arrays.get(q_index);
			 int[] p_q_array = new int[p_array.length + q_array.length];
			 System.arraycopy(p_array, 0, p_q_array, 0, p_array.length);
			 System.arraycopy(q_array, 0, p_q_array, p_array.length, q_array.length);
			 component_arrays.set(p_index, p_q_array);
			 component_arrays.remove(q_index);
			 System.out.println(p + " " + q);
			 System.out.println("Number of Connected components is: " + component_arrays.size());
			 
			 
		 }
		 
	  }
	  
  }
  private int find(int component) {
	  int[] x;
	  for(int i = 0; i<component_arrays.size(); i++){
		  x = component_arrays.get(i);
		  for(int j = 0; j<x.length; j++){
			  if(x[j] == component){
				  return i;
			  }
			  
		  }
		  
	  }
	  
	  return -1;
}
  
  private boolean is_connected(int p, int q) {
	  if(find(p) == find(q)){
		  return true;
	  }
	
	  return false;
  }
  
}


