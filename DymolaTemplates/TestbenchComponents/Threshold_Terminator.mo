within TestbenchComponents;
model Threshold_Terminator

  Modelica.Blocks.Logical.GreaterThreshold greaterThreshold(threshold=
        threshold)
    annotation (Placement(transformation(extent={{-22,-28},{-2,-8}})));
  Modelica.Blocks.Logical.TerminateSimulation terminateSimulation(condition=or1.y)
    annotation (Placement(transformation(extent={{-22,10},{58,18}})));
  Modelica.Blocks.Interfaces.RealInput u1
                                "Connector of Real input signal"
    annotation (Placement(transformation(extent={{-140,-38},{-100,2}})));
  parameter Real threshold=30 "Comparison with respect to threshold";
  Modelica.Blocks.Logical.FallingEdge fallingEdge(pre_u_start=false)
    annotation (Placement(transformation(extent={{44,-62},{64,-42}})));
  Modelica.Blocks.Logical.FallingEdge fallingEdge1(pre_u_start=false)
    annotation (Placement(transformation(extent={{42,-30},{62,-10}})));
  Modelica.Blocks.Logical.Not not1
    annotation (Placement(transformation(extent={{16,-62},{36,-42}})));
  Modelica.Blocks.Logical.Or or1
    annotation (Placement(transformation(extent={{78,-38},{98,-18}})));
  Modelica.Blocks.Interfaces.BooleanOutput term
    "Connector of Boolean output signal"
    annotation (Placement(transformation(extent={{102,-38},{122,-18}})));
equation

  connect(greaterThreshold.u, u1)
    annotation (Line(points={{-24,-18},{-120,-18}}, color={0,0,127}));

  connect(greaterThreshold.y, fallingEdge1.u) annotation (Line(points={{-1,
          -18},{20,-18},{20,-20},{40,-20}}, color={255,0,255}));
  connect(not1.y, fallingEdge.u)
    annotation (Line(points={{37,-52},{42,-52}}, color={255,0,255}));
  connect(not1.u, fallingEdge1.u) annotation (Line(points={{14,-52},{10,-52},
          {10,-18},{20,-18},{20,-20},{40,-20}}, color={255,0,255}));
  connect(fallingEdge1.y, or1.u1) annotation (Line(points={{63,-20},{70,-20},{
          70,-28},{76,-28}},  color={255,0,255}));
  connect(or1.u2, fallingEdge.y) annotation (Line(points={{76,-36},{72,-36},{72,
          -52},{65,-52}},    color={255,0,255}));
  connect(or1.y, term)
    annotation (Line(points={{99,-28},{112,-28}}, color={255,0,255}));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false, extent={{-100,-60},
            {100,40}})),                                         Diagram(
        coordinateSystem(preserveAspectRatio=false, extent={{-100,-60},{100,40}})));
end Threshold_Terminator;
