
public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		UF uf = new UF(10);
		uf.union(2, 1);
		uf.union(1, 5);
		uf.union(0, 1);
		uf.union(4, 2);
		uf.union(1, 6);
		uf.union(7, 9);

	}

}
