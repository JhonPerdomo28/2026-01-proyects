package dto;

/**
 * Author: Vinni
 */
public class Docente {
    public String nombre;
    public String apellido;

    private String obtenerNombre() {
        return nombre;
    }
    public void modificarNombre() {
        this.nombre = nombre;
    }
    private String obtenerApellido() {
        return apellido;
    }
    private void modificarApellido() {
        this.apellido = apellido;
    }
}
