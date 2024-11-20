import React from 'react';

const Body = ({
    view,
    renderTable,
    jugador,
    herramientas_basicas,
    armadura,
    comida,
    mob_pass,
    mob_neutro,
    mob_hostil,
    jefes,
    caracteristicas_jefe,
    bioma,
    estructura,
    dimension,
    agricultura,
    cubos,
}) => {
    return (
        <>
            <main className="body padding">
                {view === "inicio" && (
                    <>
                        {renderTable("jugador", jugador)}
                        {renderTable("herramientas_basicas", herramientas_basicas)}
                        {renderTable("armadura", armadura)}
                        {renderTable("comida", comida)}
                        {renderTable("mob_pass", mob_pass)}
                        {renderTable("mob_neutro", mob_neutro)}
                        {renderTable("mob_hostil", mob_hostil)}
                        {renderTable("jefes", jefes)}
                        {renderTable("caracteristicas_jefe", caracteristicas_jefe)}
                        {renderTable("bioma", bioma)}
                        {renderTable("estructura", estructura)}
                        {renderTable("dimension", dimension)}
                        {renderTable("agricultura", agricultura)}
                        {renderTable("cubos", cubos)}
                    </>
                )}

                {view === "jugador" && (
                    <>
                        {renderTable("jugador", jugador)}
                        {renderTable("herramientas_basicas", herramientas_basicas)}
                        {renderTable("armadura", armadura)}
                    </>
                )}

                {view === "mobs" && (
                    <>
                        {renderTable("mob_pass", mob_pass)}
                        {renderTable("mob_neutro", mob_neutro)}
                        {renderTable("mob_hostil", mob_hostil)}
                    </>
                )}

                {view === "jefes" && (
                    <>
                        {renderTable("jefes", jefes)}
                        {renderTable("caracteristicas_jefe", caracteristicas_jefe)}
                    </>
                )}
                {view === "estructura" && renderTable("estructura", estructura)}
                {view === "dimension" && renderTable("dimension", dimension)}
                {view === "agricultura" && renderTable("agricultura", agricultura)}
                {view === "cubos" && renderTable("cubos", cubos)}
            </main>
        </>
    );
};

export default Body;
