<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use App\Repository\PersonalRepository;
use App\Repository\InstitucionRepository;

final class CarnetController extends AbstractController
{
    #[Route('/carnet', name: 'app_carnet')]
    public function index(): Response
    {
        return $this->render('carnet/index.html.twig', [
            'controller_name' => 'CarnetController',
        ]);
    }
}
