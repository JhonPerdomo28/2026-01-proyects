package gui;

import dev.vinni.util.UtilArchivos;
import dto.Docente;

import javax.swing.*;
import java.awt.event.ActionEvent;

public class Ventana extends JFrame {
    // componentes gráficos
    private JButton btEnviar;
    private JLabel jLabel1;
    private JLabel jLabel2;
    private JLabel jLabel3;
    private JScrollPane jScrollPane1;
    private JTextArea mensajesTxt;
    private JTextField mensajeTxt;
    public Ventana() {
        this.setTitle("Ventana");
        this.iniciarComponentes();
    }
    private void iniciarComponentes() {

        this.setTitle("Registrar docente ");
        jLabel1 = new JLabel();
        jScrollPane1 = new JScrollPane();
        mensajesTxt = new JTextArea();
        mensajeTxt = new JTextField();
        jLabel2 = new JLabel();
        jLabel3 = new JLabel();
        btEnviar = new JButton();

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(null);



        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 25)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(204, 125, 0));
        jLabel1.setText("Registrar Docente ");
        jLabel1.setBounds(130, 25, 250, 30);
        getContentPane().add(jLabel1);

        jLabel2.setFont(new java.awt.Font("Verdana", 0, 14)); // NOI18N
        jLabel2.setText("Nombre:");
        jLabel2.setBounds(20, 60, 120, 30);
        getContentPane().add(jLabel2);

        jLabel3.setFont(new java.awt.Font("Verdana", 0, 14));
        jLabel3.setText("Resultado: ");
        jLabel3.setBounds(20, 180, 120, 30);
        getContentPane().add(jLabel3);


        btEnviar.setBounds(327, 140, 120, 27);
        btEnviar.setFont(new java.awt.Font("Verdana", 0, 14)); // NOI18N
        btEnviar.setText("Guardar");
        btEnviar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btEnviarActionPerformed(evt);
            }
        });
        getContentPane().add(btEnviar);

        mensajesTxt.setColumns(20);
        mensajesTxt.setRows(5);


        jScrollPane1.setViewportView(mensajesTxt);

        getContentPane().add(jScrollPane1);
        jScrollPane1.setBounds(30, 210, 410, 110);

        mensajeTxt.setFont(new java.awt.Font("Verdana", 0, 14)); // NOI18N
        getContentPane().add(mensajeTxt);
        mensajeTxt.setBounds(40, 90, 350, 30);


        setSize(new java.awt.Dimension(491, 375));
        setLocationRelativeTo(null);
    }

    private void btEnviarActionPerformed(ActionEvent evt) {
        this.guardar();
    }

    private void guardar() {
        JOptionPane.showMessageDialog(this,"Aqui se guarda ");
        String contenidoCaja = this.mensajeTxt.getText();
        Docente docente = new Docente();
        docente.nombre = contenidoCaja;
        docente.apellido = contenidoCaja;
        this.mensajesTxt.append(contenidoCaja+"\n");

        String[] dato = new String[2];
        dato[0] = docente.nombre;
        dato[1] = docente.apellido;
        UtilArchivos.guardar("archivo.txt",dato, true);

    }
}
